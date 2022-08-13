# Task 1 Software configuration

### Subtask 1 Why did I choose to participate in the challenge portfolio?


Many years ago I started my career in IT. 
Angular Core was called Angular 2.0, no one has switched to PHP7 yet, 
and js developers had to deal with callback hell. 
But I was not very lucky with projects and a year later I switched the focus 
of my activities to volunteering. For many years I helped shelters and 
homeless animals in my hometown.

But the war changed the plans of many Ukrainians.

After reviewing my IT journey, I realized that I was interested in:
* put everything in its place
* comply with all requirements
* do everything clearly and in order
* when the mechanism works like clockwork

**But at the same time, I still enjoy writing code!** 
And so I decided to study automation testing.

I haven't had a formal job for quite some time, 
which makes it hard to find a job now. 
That's why I hope to get an internship.

So thank you for this opportunity. 

Anna.

# Task 2 Selectors

### Subtask 1 Searching for selectors on the login page

<i>I avoided creating selectors with long class names whenever possible.</i>

1. h5 "Scouts Panel":
*  ``//*[text()="Scouts Panel"]``
*  ``//h5 or //form//h5`` or other variations with h5 =)
*  ``//*[@class="MuiTypography-root MuiTypography-h5 MuiTypography-gutterBottom"]``
2. Label "Login":
* ``//*[@id="login-label"]``
* ``//label[text() = "Login"]``
* ``//label[@for = "login"]``
* ``(//label/text())[1]``
3. Input "Login":
* ``//*[@id="login"]``
* ``//input[@name="login"]``
* ``//*[@id="login-label"]/following-sibling::div/input``
4. Label "Password":
* ``//*[@id="password-label"]``
* ``(//label/text())[2]``
* ``//label[@for = "password"]``
5. Input "Password":
* ``//*[@id="password"]``
* ``//input[@name="password"]``
* ``//*[@id="password-label"]/following-sibling::div/input``
6. Link "Remind Password":
* ``//a/text()``
* ``//div[@class="MuiCardContent-root"]/a``
* ``//h5/following-sibling::a``
7. Button with localization:
* Button itself:
``//div[@class = "MuiCardActions-root"]//div[@role = "button"]``
* Input with value:
``//input[@class = "MuiSelect-nativeInput"]``
* And we also have a dropdown with languages:
``//*[@id="menu-"]//ul/li[1]`` or [2] for 2-d element
* Or another version for languages: 
``//ul/li[text()="Polski"]`` or ``//ul/li[text()="English"]``
8. Sign in button:
* ``//button[@type="submit"]``
* ``//button[descendant::span[text()]]``
* ``//div[@class="MuiCardActions-root"]/button``








