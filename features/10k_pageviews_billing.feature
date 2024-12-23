Feature: 10k pageviews monthly billing
    Scenario: 10k pageviews monthly billing
        Given visit bitcoin price calculator
        When slide to 10k pageviews
        Then the price should be $8.00 / month
        When switch to yearly billing
        Then the price should be $6.00 / year