Feature: 50k pageviews monthly billing
    Scenario: 50k pageviews monthly billing
        Given visit bitcoin price calculator
        When slide to 50k pageviews
        Then the price should be $12.00 / month
        When switch to yearly billing
        Then the price should be $9.00 / year