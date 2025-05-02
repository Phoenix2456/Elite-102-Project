-- Modify email
UPDATE account
SET modify_email = "Ray@gmail.com", modify_passcode = "Nina"
WHERE id = 1

-- Modify passcode
UPDATE account
SET modify_email = "Ray@gmail.com", modify_passcode = "Nina"
WHERE id = 1

-- Account Deletion
DELETE FROM accounts WHERE 