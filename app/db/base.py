import uuid
import hashlib
import json
from datetime import datetime

from sqlalchemy import event
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func


class TableBase(DeclarativeBase):
    """
    Base class for all tables.
    This class includes common fields such as id, created_at, and updated_at.
    It also includes a configuration class for ORM mode and JSON encoding.
    """

    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=uuid.uuid4, doc="Primary key as a UUID."
    )

    created_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(datetime.timezone.utc),
        server_default=func.now(),
        doc="Timestamp when the record was created.",
    )
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False,
        default=datetime.now(datetime.timezone.utc),
        onupdate=datetime.now(datetime.timezone.utc),
        server_default=func.now(),
        doc="Timestamp when the record was last updated.",
    )
    ckecksum: Mapped[str] = mapped_column(
        String(128),
        nullable=False,
        server_default="",
        doc="SHA-256 checksum for data integrity.",
    )

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    @staticmethod
    def generate_sha256_hash_from_file(file_path: str) -> str:
        """Generates a SHA-256 hash of the file contents.
        Args: file_path (str): File path.
        Returns: str: Hash in SHA-256 format.
        """
        hash_object = hashlib.sha256()
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                hash_object.update(chunk)
        return hash_object.hexdigest()

    @staticmethod
    def generate_sha256_hash_from_json(data: dict) -> str:
        """Generates a SHA-256 hash of the json contents.
        Args: data (str): json path.
        Returns: str: Hash in SHA-256 format.
        """
        json_string = json.dumps(
            data, sort_keys=True
        )  # Сортуємо ключі для консистентності
        hash_object = hashlib.sha256(json_string.encode())
        return hash_object.hexdigest()


@event.listens_for(TableBase, "before_insert")
def set_checksum(mapper, connection, target):
    """
    Automatically sets a checksum before inserting a record into the database.
    """
    if hasattr(target, "file_path") and target.file_path:  # Якщо є шлях до файлу
        target.checksum = target.generate_sha256_hash_from_file(target.file_path)
    elif hasattr(target, "json_data") and target.json_data:  # Якщо є JSON-дані
        target.checksum = target.generate_sha256_hash_from_json(target.json_data)
    else:
        raise ValueError(
            "Either 'file_path' or 'json' must be provided to generate a checksum."
        )
