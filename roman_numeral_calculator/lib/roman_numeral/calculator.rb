# frozen_string_literal: true

require_relative './validations'

module RomanNumeral
  module Calculator
    extend Validations

    def self.evaluate(expression)
      validate_expression(expression)
      expression
    end
  end
end
