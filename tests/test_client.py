from io import BytesIO
from unittest.mock import patch, MagicMock

import pandas as pd
import pytest
import requests

from src.client import DataGovUAClient


class TestDataGovUAClient:
    def setup_method(self):
        self.dataset_id = "c445c6ea-f0c3-4167-abb1-5afb4a0e5499"
        self.resource_id = "d55eebcf-4660-4919-96b3-4894be5a6cda"
        self.resource_url = "https://.../nuclear_safety_q4_2024.xlsx"

        self.mock_metadata_response = {
            "help": "https://data.gov.ua/api/3/action/help_show?name=package_show",
            "success": True,
            "result": {
                "resources": [
                    {
                        "id": self.resource_id,
                        "url": self.resource_url,
                    },
                    {
                        "id": "afa0c772-2554-4b9a-98b4-980e54b1e21a",
                        "url": "https://.../pasport-naboru-danikh.xlsx",
                    },
                ],
            },
        }

        self.mock_response = MagicMock()
        self.mock_response.status_code = 200
        self.mock_response.raise_for_status.return_value = None
        self.mock_response.json.return_value = self.mock_metadata_response

    @patch("requests.get")
    def test_fetch_metadata(self, mock_get):
        mock_get.return_value = self.mock_response

        client = DataGovUAClient(dataset_id=self.dataset_id)
        client.fetch_metadata()

        assert client.metadata == self.mock_metadata_response
        assert client.resources == self.mock_metadata_response["result"]["resources"]


    @patch("requests.get")
    def test_fetch_metadata_http_error(self, mock_get):
        mock_get.return_value = MagicMock()
        mock_get.return_value.raise_for_status.side_effect = requests.HTTPError("404")

        client = DataGovUAClient(dataset_id=self.dataset_id)

        with pytest.raises(requests.HTTPError):
            client.fetch_metadata()

    @patch("requests.get")
    def test_get_resource_url_success(self, mock_get):
        mock_get.return_value = self.mock_response

        client = DataGovUAClient(self.dataset_id)
        client.fetch_metadata()

        url = client.get_resource_url(self.resource_id)
        assert url == self.resource_url

    @patch("requests.get")
    def test_get_resource_url_not_found(self, mock_get):
        mock_get.return_value = self.mock_response

        client = DataGovUAClient(self.dataset_id)
        client.fetch_metadata()

        with pytest.raises(KeyError, match="not found"):
            client.get_resource_url("non-existent-id")

    @patch("requests.get")
    def test_load_dataframe_success(self, mock_get):
        # Create excel file for download.
        df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        buffer = BytesIO()
        df.to_excel(buffer, index=False)
        buffer.seek(0)

        # Mock requests response.
        mock_response = MagicMock()
        mock_response.content = buffer.read()
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        # Test the function
        client = DataGovUAClient(self.dataset_id)
        result_df = client.load_dataframe(self.resource_url)
        pd.testing.assert_frame_equal(result_df, df)
