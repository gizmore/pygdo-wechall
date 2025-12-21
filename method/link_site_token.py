import base64
import hashlib

from gdo.base.Application import Application
from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDO_User import GDO_User
from gdo.core.GDT_Base64 import GDT_Base64
from gdo.core.GDT_Hash import GDT_Hash
from gdo.wechall.WC_Site import WC_Site


class link_site_token(Method):

    def gdo_parameters(self) -> list[GDT]:
        return [
            GDT_Base64('token').not_null(),
        ]

    @classmethod
    def token(cls, user: GDO_User, site: WC_Site, onsite_name: str, email: str) -> str:
        secret = Application.config('core.secret')
        payload = f"{user.get_id()}:{site.get_id()}:{onsite_name}:{email}"
        token = GDT_Base64.encode(payload)
        hash = GDT_Hash().hash(token)
        payhashlib.sha3_256(payload.encode()).hexdigest()