from dataclasses import dataclass, field


@dataclass
class UserRequest:

    goal: str

    filters: dict = field(default_factory=dict)

    outputs: list[str] = field(default_factory=list)      #What outputs does the user want