# frozen_string_literal: true

require_relative './validations'
require_relative './converter'

module RomanNumeral
  module Calculator
    extend Validations

    def self.evaluate(expression)
      converted_expression = convert_to_numerical_expression(expression.dup)
      result = evaluate_numerical_expression(converted_expression)
      validate_integer_result(result)
      Converter.to_roman_numeral(result.to_i)
    end

    def self.convert_to_numerical_expression(expression)
      validate_roman_numeral_expression(expression)
      expression.scan(/([IVXLCDM]+)/).each do |(roman_numeral)|
        expression.sub!(roman_numeral, Converter.to_integer(roman_numeral).to_f.to_s)
      end
      expression.gsub('^', '**')
    end
    private_class_method :convert_to_numerical_expression

    def self.evaluate_numerical_expression(expression)
      validate_numerical_expression(expression)
      # As a rule, using `eval` is risky as malicious code can be executed accidentally,
      # but at this point of the execution the expression has been validated to ensure it is a
      # purely numerical expression.
      # rubocop:disable Security/Eval
      eval(expression)
      # rubocop:enable Security/Eval
    rescue SyntaxError => _e
      raise ArgumentError,
            'The roman numeral calculator can only process expressions with evaluatable syntax.'
    end
    private_class_method :evaluate_numerical_expression
  end
end
