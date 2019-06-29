# Habit Tracker

For this project, you will be working in pairs to build a Django application that you can use to help track and reinforce daily habits.

## Requirements and Goals

* Your application should be styled. It should be usable and aesthetically neutral, at a minimum.
* Your application should be able to run from scratch by downloading the repo, running `pipenv install`, `python manage.py migrate`, and `python manage.py runserver`.
* When working on this project, use feature branches and pull requests to manage your workflow.
* When working on this project, try pair programming.

### Goal 0: Setup

* **Already done!** Your application should have a User model (the built-in one is fine) and have registration and login. You do not need to have users click an email link to finish registration -- the simple flow from django-registration-redux is fine.
* You need to create a Django app. Run `./manage.py startapp <appname>`. If you can't think of a name for your app, `core` is fine.
* Edit `templates/base.html` to customize your project's style.

### Goal 1: Habits

* Users should be able to create a new habit tracker. Each habit should have a name and a target or goal. What is this "target"? Each habit should have a daily number of some action you want to do. Some examples:
  * I want to walk 1000 steps daily
  * I want to write 100 lines of code daily
  * I want to talk to 2 new people each day
  * I want to read 200 pages daily
  * I want to sleep 8 hours daily
* Once you have habits, you should be able to make a daily record of your activity on each habit. That record should contain a date and a number for that date.
* A user can only have one record per day per habit. You will need to use [the `unique_together` option](https://docs.djangoproject.com/en/2.2/ref/models/options/#unique-together) to enforce this.
* Optimally, users can edit/update records and add records for previous days.
* Make your interface for this feature as easy to use as possible. For example, if you can choose the date for your record, have it default to the current date.
* On the detail page for a habit, you should be able to see all the records for that habit in an HTML table. Show the user whether they met their goal for that day visually somehow -- maybe via colors. Think about accessibility here -- how would a user that can't see know whether they met their goal each day?

#### Stretch goals

* On the detail page for a habit, show the best day for that habit, and the average day for that habit.
* When you list the records for a habit, show any days that don't have a record that are between the first and last record. For example, if there's a record for June 28 and a record for June 30, show June 29 as well and highlight that it has missing data. Provide a way to fill in that data easily.
* Add the ability to have "negative habits." These habits should have a goal you want to get under. For example:
  * I want to watch less than 60 minutes of TV daily
  * I want to eat less than 15 jellybeans a day
  * I want to say less than 3 curse words a day
* If a user is missing a record for a habit for the previous day, show them a message on their dashboard that lets them know and asks them to put in the record. Make it easy to jump from that message to the form to enter the data.
* Use the [new `constraints` option for models](https://docs.djangoproject.com/en/2.2/ref/models/constraints/) with `UniqueConstraint` to make the habit records unique by user, habit, and day.

### Goal 2: Accountability

* Users can add observers to a habit. These observers can see all the data for that habit, but not edit or add data.
* These observers can be added via username or email address (your choice). In a real application, we would always use email address and then email the person if they do not yet have an account on our site, adding them as an observer when they sign up. This is complicated, and you don't need to do it for this project. Instead, just let the user adding an observer know that the observer doesn't have an account.
* Users can see a list of their own habits and others' habits they are observing on their dashboard.
* When an observer looks at a habit they are observing, don't forget to show the name or username of the user the habit belongs to.

#### Stretch goals

* Observers can add comments to a daily habit record. That is, if Amari is tracking their lines of code, and they wrote 120 lines yesterday, and Blake is an observer on this habit, Blake can write a comment that says "Great job!" for that particular day.
