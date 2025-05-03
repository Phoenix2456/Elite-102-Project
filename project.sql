-- Modify email
UPDATE account
SET email = "Ray@gmail.com"
WHERE id = 1

-- Modify passcode
UPDATE account
SET passcode = "Nina"
WHERE id = 1

-- Account Deletion
DELETE FROM accounts WHERE 


-- Deposite


-- Withdraw


-- Create Account
INSERT INTO account (email, column2, column3, ...)
VALUES (value1, value2, value3, ...);


-- Existing Account
--SELECT email
--FROM account
--WHERE EXISTS
--(SELECT email FROM account WHERE condition);