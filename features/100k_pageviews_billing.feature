Feature: 100k pageviews monthly billing
    Scenario: 100k pageviews monthly billing
        Given visit bitcoin price calculator
        When slide to 100k pageviews
        Then the price should be $16.00 / month
        When switch to yearly billing
        Then the price should be $12.00 / year in 100k