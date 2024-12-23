Feature: 1m pageviews monthly billing
    Scenario: 1m pageviews monthly billing
        Given visit bitcoin price calculator
        When slide to 1m pageviews
        Then the price should be $36.00 / month
        When switch to yearly billing
        Then the price should be $27.00 / year