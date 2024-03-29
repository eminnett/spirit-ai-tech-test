# frozen_string_literal: true

require_relative './validations'
require_relative './converter'

module RomanNumeral
  # The Calculator module handles the evaluation of roman numeral mathematical expressions. As long
  # as the `expression` is a valid roman numeral mathematical expression and the calculated result
  # is an integer, the calculator will return the result of the expression as a roman numeral.
  #
  # Example Usage:
  # RomanNumeral::Calculator.evaluate('(V + IX) * III') => 'XLII'
  module Calculator
    extend Validations

    def self.evaluate(expression)
      converted_expression = convert_to_numerical_expression(expression.dup)
      result = evaluate_numerical_expression(converted_expression)
      validate_integer_result(result)
      evaluation = ''
      if result.negative?
        evaluation += '-'
        result *= -1
      end
      evaluation += Converter.to_roman_numeral(result.to_i)
      evaluation
    end

    private_class_method def self.convert_to_numerical_expression(expression)
      validate_roman_numeral_expression(expression)
      expression.scan(/([IVXLCDM]+)/).each do |(roman_numeral)|
        expression.sub!(roman_numeral, Converter.to_integer(roman_numeral).to_f.to_s)
      end
      expression.gsub('^', '**')
    end

    private_class_method def self.evaluate_numerical_expression(expression)
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
  end
end
