from abc import ABC, abstractmethod


class TrickBase(ABC):
    def __init__(self):
        # Each subclass must generate a question and an answer.
        required_attrs = ["question", "answer"]

        for attr in required_attrs:
            if not hasattr(self, attr):
                raise NotImplementedError(
                    f"Subclass '{self.__class__.__name__}' must define the '{attr}' constant."
                )

    @abstractmethod
    def trick_type_message(self):
        pass
