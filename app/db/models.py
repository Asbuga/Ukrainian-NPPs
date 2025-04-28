from datetime import datetime

from base import TableBase
from sqlalchemy import Boolean, ForeignKey, String, func
from sqlalchemy.orm import Mapped, mapped_column


class Dataset(TableBase):
    """
    Dataset model representing a dataset in the database.
    Inherits from TableBase which includes common fields.
    """
    dataset_id: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    source_url: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"Dataset(id={self.id!r}, dataset_id={self.dataset_id!r}, title={self.title!r})"


class Resource(TableBase):
    """
    Resource model representing a resource in the dataset metadata.
    Inherits from TableBase which includes common fields.
    """
    dataset_id: Mapped[str] = mapped_column(
        ForeignKey("dataset.dataset_id"), nullable=False, index=True
    )
    resource_id: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    format: Mapped[str] = mapped_column(String(8), nullable=False)
    source_url: Mapped[str] = mapped_column(String(255), nullable=False)
    file_name: Mapped[str] = mapped_column(String(255), nullable=True)
    downloaded_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(datetime.timezone.utc),
        server_default=func.now(),
        doc="Timestamp when the record was downloaded.",
    )
    chart: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    def __repr__(self) -> str:
        return (
            f"Resource(id={self.resource_id!r}, dataset_id={self.dataset_id!r}, "
            f"format={self.format!r}, source_url={self.source_url!r}, "
            f"file_name={self.file_name!r}, downloaded_at={self.downloaded_at!r}, "
            f"chart={self.chart!r})"
        )


class Chart(TableBase):
    """
    Chart model representing a chart in the dataset metadata.
    Inherits from TableBase which includes common fields.
    """
    dataset_id: Mapped[str] = mapped_column(
        ForeignKey("dataset.dataset_id"), nullable=False, index=True
    )
    resource_id: Mapped[str] = mapped_column(
        ForeignKey("resource.resource_id"), nullable=False, index=True
    )
    format: Mapped[str] = mapped_column(String(8), nullable=False)
    source_url: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"Chart(id={self.id!r}, resource_id={self.resource_id!r}, format={self.format!r})"


class Logs(TableBase):
    """
    Logs model representing logs in the database.
    Inherits from TableBase which includes common fields.
    """
    message: Mapped[str] = mapped_column(String(255), nullable=False)
    level: Mapped[str] = mapped_column(String(10), nullable=False)
    timestamp: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(datetime.timezone.utc),
        server_default=func.now(),
        doc="Timestamp when the log was created.",
    )

    def __repr__(self) -> str:
        return (
            f"Logs(id={self.log_id!r}, message={self.message!r}, level={self.level!r})"
        )
