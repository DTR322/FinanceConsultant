from fastapi import APIRouter
from fastapi.params import Depends

from app.finance.dao import TransactionDAO
from app.finance.rb import RBTransaction
from app.finance.schemas import STransactionCreate, STransaction

router = APIRouter(
    prefix="/finance",
    tags=["работа с транзакциями"]
)


@router.get("/", summary="получить все транзакции")
async def get_all_transactions(request_body: RBTransaction = Depends()) -> list[STransaction]:
    return await TransactionDAO.find_all()

@router.get("/{id}", summary="получить одну транзакцию по id")
async def get_transaction_by_id(transaction_id: int) -> STransaction | dict:
    result = await TransactionDAO.find_one_or_none_by_id(transaction_id)
    if result is None:
        return {'message': f"Транзакция с ID {transaction_id} не найдена!"}
    return result


@router.post("/add", summary="добавить транзакцию")
async def add_transaction(transaction: STransactionCreate) -> dict:
    check = await TransactionDAO.add(**transaction.dict())
    if check:
        return {'message': "Транзакция Успешно добавлена!"}

