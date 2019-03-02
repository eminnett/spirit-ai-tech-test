# frozen_string_literal: true

module RomanNumeral
  module Calculator
    def self.evaluate(expression)
      validate_expression(expression)
      expression
    end

    def self.validate_expression(expression)
      return true if %r{^[IVXLCDM\(\)\^/\*\+\-\s]+$}.match?(expression)

      raise ArgumentError, "'#{expression}' is not a calculable expression"
    end
    private_class_method :validate_expression
  end
end
