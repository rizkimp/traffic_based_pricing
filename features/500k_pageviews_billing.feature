Feature: 500k pageviews monthly billing
    Scenario: 500k pageviews monthly billing
        Given visit bitcoin price calculator
        When slide to 500k pageviews
        Then the price should be $24.00 / month
        When switch to yearly billing
        Then the price should be $18.00 / year