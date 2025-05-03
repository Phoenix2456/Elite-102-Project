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


-- Deposit
INSERT INTO account (check_balance)
VALUES (value1, value2, value3, ...);

-- Withdraw


-- Create Account
INSERT INTO account (email, passcode)
VALUES ("Briane@gmail.com", "Dejavu");


-- Existing Account
--SELECT email
--FROM account
--WHERE EXISTS
--(SELECT email FROM account WHERE condition);