import uuid

from sqlalchemy import String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.audit_mixin import AuditMixin
from app.models.base_uuid import UUIDPrimaryKeyMixin
from app.models.soft_delete_mixin import SoftDeleteMixin


class User(Base, AuditMixin,UUIDPrimaryKeyMixin, SoftDeleteMixin):
    __tablename__ = "users"

    

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    memberships = relationship(
        "Membership",
        back_populates="user"
    )
