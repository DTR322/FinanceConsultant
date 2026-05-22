from fastapi import APIRouter, Depends

from app.users.dependencies import get_current_user
from app.users.models import User
from app.wallets.dao import WalletsDAO
from app.wallets.models import Wallet
from app.wallets.rb import RBWalletCreate, RBWalletFilter
from app.wallets.schemas import SWallet

router = APIRouter(prefix='/wallets', tags=['работа со счетами и картами'])


@router.post("/create")
async def create_wallet(wallet: RBWalletCreate, user: User = Depends(get_current_user)):

    created_wallet = await WalletsDAO.add(
        user_id = user.id
        **wallet.model_dump()
    )
    return created_wallet

@router.get("/all")
async def get_wallets(filter_by: RBWalletFilter, user: User = Depends(get_current_user)) -> list[Wallet]:

    return await WalletsDAO.find_all(user_id=user.id, **filter_by.to_dict())

@router.get("/{id}")
async def get_wallet()




