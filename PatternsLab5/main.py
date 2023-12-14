from cryptography.fernet import Fernet
from fastapi import FastAPI

from schemas.BankCustomer import BankCustomer, PersonalInfo
from schemas.BankInfo import BankInfo
from schemas.Credit_Cart import GoldenCreditCard, CorporateCreditCard

app = FastAPI()

encryption_key = Fernet.generate_key()


GoldenCard = GoldenCreditCard(
    customer_name="Denis Just",
    account_number="4148 4128 6413 1243",
    credit_limit=8888.0,
    grace_period=80,
    cvv="732",
    encryption_key=encryption_key
)


CorporateCard = CorporateCreditCard(
    customer_name="Denis Just",
    account_number="4141 1585 1242 5122",
    credit_limit=12000.0,
    grace_period=50,
    cvv="135",
    encryption_key=encryption_key
)

GoldenCardDetails = GoldenCard.give_details()
CorporateCardDetails = CorporateCard.give_details()

bank_info = BankInfo(
    bank_name="Mega Ultra Bank",
    holder_name="Denis Just",
    accounts_number=["4148 4128 6413 1243", "4141 1585 1242 5122"],
    credit_history={
        'golden_card': {
            'account_number': GoldenCardDetails['account_number'],
            'credit_limit': GoldenCardDetails['credit_limit'],
            'grace_period': GoldenCardDetails['grace_period'],
        },
        'corporate_card': {
            'account_number': CorporateCardDetails['account_number'],
            'credit_limit': CorporateCardDetails['credit_limit'],
            'grace_period': CorporateCardDetails['grace_period'],
        },
    }
)


personal_info = PersonalInfo()


bank_customer = BankCustomer(
    personal_info=personal_info,
    bank_details=bank_info
)


@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI application works now!"}


@app.post("/enhanced_credit_card")
async def get_enhanced_credit_card():
    return {"enhanced_credit_card_details": GoldenCard.give_details()}


@app.post("/bank_customer")
async def get_bank_customer():
    return {"bank_customer_details": bank_customer.give_details()}
