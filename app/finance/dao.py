from app.dao.base import BaseDAO
from app.finance.models import Transaction


class TransactionDAO(BaseDAO):
    model = Transaction