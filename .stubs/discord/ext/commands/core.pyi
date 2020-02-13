from inspect import Parameter

from .context import Context
from .cooldowns import CooldownMapping, BucketType, Cooldown
from .cog import Cog
from ._types import _BaseCommand

from typing import (
    Any,
    Optional,
    Union,
    Callable,
    Dict,
    Iterator,
    Coroutine,
    Type,
    ValuesView,
    List,
    TypeVar,
    Mapping,
    Generic,
    overload,
)

_CT = TypeVar("_CT", bound=Context)
_CheckType = Union[Callable[[_CT], bool], Callable[[_CT], Coroutine[Any, Any, bool]]]
_CoroType = Callable[..., Coroutine[Any, Any, Any]]
_C = TypeVar("_C", bound=_CoroType)
_CMD = TypeVar("_CMD", bound=Command)
_F = TypeVar("_F", bound=Union[_CoroType, Command[Any]])

class Command(_BaseCommand, Generic[_CT]):
    name: str
    callback: _CoroType
    help: str
    brief: str
    usage: str
    aliases: List[str]
    enabled: bool
    parent: Optional[Command[_CT]]
    checks: List[_CheckType]
    description: str
    hidden: bool
    rest_is_raw: bool
    ignore_extra: bool
    cooldown_after_parsing: bool
    params: Mapping[str, Parameter]
    _buckets: CooldownMapping
    cog: Optional[Cog[_CT]]
    def __init__(
        self,
        func: _CoroType,
        *,
        name: str = ...,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: List[str] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        cooldown_after_parsing: bool = ...,
        checks: List[_CheckType] = ...,
        cooldown: Cooldown = ...,
        parent: _BaseCommand = ...,
        cog: Optional[Cog[_CT]] = ...,
    ) -> None: ...
    def add_check(self, func: _CheckType) -> None: ...
    def remove_check(self, func: _CheckType) -> None: ...
    def update(
        self,
        name: str = ...,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: List[str] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        cooldown_after_parsing: bool = ...,
    ) -> None: ...
    def copy(self: _CMD) -> _CMD: ...
    async def dispatch_error(self, ctx: _CT, error: Exception) -> None: ...
    async def do_conversion(
        self, ctx: _CT, converter: Any, argument: str, param: Parameter
    ) -> Any: ...
    async def transform(self, ctx: _CT, param: Parameter) -> Any: ...
    @property
    def clean_params(self) -> Mapping[str, Parameter]: ...
    @property
    def full_parent_name(self) -> str: ...
    @property
    def parents(self) -> List[Command[_CT]]: ...
    @property
    def root_parent(self) -> Optional[Command[_CT]]: ...
    @property
    def qualified_name(self) -> str: ...
    async def call_before_hooks(self, ctx: _CT) -> None: ...
    async def call_after_hooks(self, ctx: _CT) -> None: ...
    async def prepare(self, ctx: _CT) -> None: ...
    def is_on_cooldown(self, ctx: _CT) -> bool: ...
    def reset_cooldown(self, ctx: _CT) -> None: ...
    async def invoke(self, ctx: _CT) -> None: ...
    async def reinvoke(self, ctx: _CT, *, call_hooks: bool = ...) -> None: ...
    def error(self, coro: _C) -> _C: ...
    def before_invoke(self, coro: _C) -> _C: ...
    def after_invoke(self, coro: _C) -> _C: ...
    @property
    def cog_name(self) -> Optional[str]: ...
    @property
    def short_doc(self) -> str: ...
    @property
    def signature(self) -> str: ...
    async def can_run(self, ctx: _CT) -> bool: ...

class GroupMixin(Generic[_CT]):
    all_commands: Dict[str, Command[_CT]]
    case_insensitive: bool
    @property
    def commands(self) -> ValuesView[Command[_CT]]: ...
    def recursively_remove_all_commands(self) -> None: ...
    def add_command(self, command: Command[_CT]) -> None: ...
    def remove_command(self, name: str) -> Optional[Command[_CT]]: ...
    def walk_commands(self) -> Iterator[Command[_CT]]: ...
    def get_command(self, name: str) -> Optional[Command[_CT]]: ...
    def command(
        self,
        name: Optional[str] = ...,
        *,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: List[str] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        cooldown_after_parsing: bool = ...,
    ) -> Callable[[_CoroType], Command[_CT]]: ...
    def group(
        self,
        name: str = ...,
        *,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: List[str] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        cooldown_after_parsing: bool = ...,
        invoke_without_command: bool = ...,
        case_insensitive: bool = ...,
    ) -> Callable[[_CoroType], Group[_CT]]: ...

_G = TypeVar("_G", bound=Group)

class Group(GroupMixin[_CT], Command[_CT]):
    invoke_without_command: bool
    def __init__(
        self,
        *,
        name: str = ...,
        enabled: bool = ...,
        help: Optional[str] = ...,
        brief: Optional[str] = ...,
        usage: Optional[str] = ...,
        aliases: List[str] = ...,
        description: str = ...,
        hidden: bool = ...,
        rest_is_raw: bool = ...,
        ignore_extra: bool = ...,
        cooldown_after_parsing: bool = ...,
        invoke_without_command: bool = ...,
        case_insensitive: bool = ...,
    ) -> None: ...
    def copy(self: _G) -> _G: ...

@overload
def command(
    name: Optional[str] = ...,
    *,
    enabled: bool = ...,
    help: Optional[str] = ...,
    brief: Optional[str] = ...,
    usage: Optional[str] = ...,
    aliases: List[str] = ...,
    description: str = ...,
    hidden: bool = ...,
    rest_is_raw: bool = ...,
    ignore_extra: bool = ...,
    cooldown_after_parsing: bool = ...,
) -> Callable[[_CoroType], Command[Any]]: ...
@overload
def command(
    name: Optional[str] = ...,
    cls: Optional[Type[Command[_CT]]] = ...,
    *,
    enabled: bool = ...,
    help: Optional[str] = ...,
    brief: Optional[str] = ...,
    usage: Optional[str] = ...,
    aliases: List[str] = ...,
    description: str = ...,
    hidden: bool = ...,
    rest_is_raw: bool = ...,
    ignore_extra: bool = ...,
    cooldown_after_parsing: bool = ...,
) -> Callable[[_CoroType], Command[_CT]]: ...
@overload
def group(
    name: str = ...,
    *,
    enabled: bool = ...,
    help: Optional[str] = ...,
    brief: Optional[str] = ...,
    usage: Optional[str] = ...,
    aliases: List[str] = ...,
    description: str = ...,
    hidden: bool = ...,
    rest_is_raw: bool = ...,
    ignore_extra: bool = ...,
    cooldown_after_parsing: bool = ...,
    invoke_without_command: bool = ...,
    case_insensitive: bool = ...,
) -> Callable[[_CoroType], Group[Any]]: ...
@overload
def group(
    name: str = ...,
    *,
    cls: Optional[Type[Group[_CT]]] = ...,
    enabled: bool = ...,
    help: Optional[str] = ...,
    brief: Optional[str] = ...,
    usage: Optional[str] = ...,
    aliases: List[str] = ...,
    description: str = ...,
    hidden: bool = ...,
    rest_is_raw: bool = ...,
    ignore_extra: bool = ...,
    cooldown_after_parsing: bool = ...,
    invoke_without_command: bool = ...,
    case_insensitive: bool = ...,
) -> Callable[[_CoroType], Group[Any]]: ...
def check(predicate: _CheckType) -> Callable[[_F], _F]: ...
def has_role(item: Union[int, str]) -> Callable[[_F], _F]: ...
def has_any_role(*items: Union[int, str]) -> Callable[[_F], _F]: ...
def bot_has_role(item: Union[int, str]) -> Callable[[_F], _F]: ...
def bot_has_any_role(*items: Union[int, str]) -> Callable[[_F], _F]: ...
def has_permissions(**perms: bool) -> Callable[[_F], _F]: ...
def bot_has_permissions(**perms: bool) -> Callable[[_F], _F]: ...
def dm_only() -> Callable[[_F], _F]: ...
def guild_only() -> Callable[[_F], _F]: ...
def is_owner() -> Callable[[_F], _F]: ...
def is_nsfw() -> Callable[[_F], _F]: ...
def cooldown(rate: int, per: float, type: BucketType = ...) -> Callable[[_F], _F]: ...
def _convert_to_bool(argument: str) -> bool: ...
