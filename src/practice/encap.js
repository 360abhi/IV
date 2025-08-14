class BankAccount{
    #balance = 0
    deposit(amount){
        this.#balance += amount
    }
    getBalance(){
        return this.#balance
    }
}

const bank = new BankAccount()
bank.deposit(100)
console.log(bank.getBalance())
// console.log(bank.#balance)