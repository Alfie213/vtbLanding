import { BankOperation } from './BankOperation.js'

const handlingDelay = 500; // 0.5 seconds.

export class BankWindow {
    constructor(id) {
        this.id = id;
        // this.isWorking = false;
        // this.workingTime = 0;
        this.remainingHandleTime = 0;
    }

    /** @param {BankOperation} operation **/
    async HandleBankOperation(operation, callback) {
        // this.workingTime = operation.operationType;
        // this.isWorking = true;
        // console.log(`start ${this.isWorking }`);
        this.remainingHandleTime = operation.operationType;
        console.log(`BankWindow ${this.id} started handling BankOperation. Time of operation - ${operation.operationType / 1000} seconds.`);
        while (true) {
            await new Promise((resolve) => setTimeout(resolve, handlingDelay));
            this.remainingHandleTime -= handlingDelay;
            if (this.remainingHandleTime <= 0) {
                callback(this.id);
                // this.isWorking = false;
                // this.workingTime = 0;
                return;
            }
            // await new Promise((resolve) => setTimeout(resolve, operation.operationType));
        }
    }
}