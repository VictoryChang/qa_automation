# Test Case Outline

Note: This can be in an automated platform or documented in a spreadsheet or other form

- **Test ID:** TC001
- **Test Priority:** High (P1)
- **Feature Name:** OrangeHRM Login Page
- **Feature Link:** https://company.jira.com/Feature001
- **Summary:** Verify that I as a user can log into the OrangeHRM portal using my valid username and password
- **Precondition:**
  - An account has already been created for the user Admin
- **Test Steps:**
  - Go to: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
  - Enter username: Admin
  - Enter password: admin123
  - Click Login
- **Test Data:**
  - Username: Admin
  - Password: admin123
- **Expected Results:**
  - The browser navigates to: https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index
  - You are logged in and can see the management dashboard
- **Actual Results:**
  - As expected
- **Postcondition:** Not applicable
- **Status:** Pass (Fail/Blocked)
- **Defect Link:** https://company.jira.com/BugFor001
- **Automated?** Yes (No)