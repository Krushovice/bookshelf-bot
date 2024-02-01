__all__ = ("router",)


from aiogram import Router

from .base_commands import router as base_commands_router
from .user_commands import router as user_commands_router
from .crud_commands import router as crud_commands_router
from .questionary import router as register_router


router = Router(name=__name__)
router.include_routers(
    base_commands_router,
    user_commands_router,
    crud_commands_router,
    register_router,
)
