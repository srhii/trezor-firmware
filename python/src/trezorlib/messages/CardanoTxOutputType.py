# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .CardanoAddressParametersType import CardanoAddressParametersType
from .CardanoAssetGroupType import CardanoAssetGroupType

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class CardanoTxOutputType(p.MessageType):

    def __init__(
        self,
        *,
        token_bundle: List[CardanoAssetGroupType] = None,
        address: str = None,
        amount: int = None,
        address_parameters: CardanoAddressParametersType = None,
    ) -> None:
        self.token_bundle = token_bundle if token_bundle is not None else []
        self.address = address
        self.amount = amount
        self.address_parameters = address_parameters

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('address', p.UnicodeType, None),
            3: ('amount', p.UVarintType, None),
            4: ('address_parameters', CardanoAddressParametersType, None),
            5: ('token_bundle', CardanoAssetGroupType, p.FLAG_REPEATED),
        }
