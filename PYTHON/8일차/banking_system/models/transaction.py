class Transaction:

    while True:
        transaction_menu = input("[입금]과 [출금] 중 원하시는 서비스를 입력해 주세요, 종료를 원하시면 [종료]를 입력해 주세요.")
        if transaction_menu == "종료":
            break

        def __init__(self, transaction_type : str, amount : int, balance : int) -> None:
            self.transaction_type = transaction_type
            self.amount = amount
            self.balance = balance

        def __str__(self) -> str:
            return f"{self.transaction_type} : {self.amount}원 , 잔고 : {self.balance}원 입니다."
        
        def to_tule(self) -> tuple:
            return self.transaction_type, self.amount, self.balance
        break
