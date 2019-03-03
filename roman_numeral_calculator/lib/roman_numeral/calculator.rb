# frozen_string_literal: true

require_relative './validations'
require_relative './converter'

module RomanNumeral
  module Calculator
    extend Validations

    def self.evaluate(expression)
      validate_roman_numeral_expression(expression)
      converted_expression = expression.dup
      expression.scan(/([IVXLCDM]+)/).each do |(roman_numeral)|
        converted_expression.sub!(roman_numeral, Converter.to_integer(roman_numeral).to_f.to_s)
      end
      converted_expression.gsub!('^', '**')
      begin
        validate_numerical_expression(converted_expression)
        # As a rule, using `eval` is risky as malicious code can be executed accidentally,
        # but at this point of the execution the expression has been validated to ensure it is a
        # purely numerical expression.
        # rubocop:disable Security/Eval
        result = eval(converted_expression)
        # rubocop:enable Security/Eval
      rescue SyntaxError => _e
        raise ArgumentError,
              'The roman numeral calculator can only process expressions with evaluatable syntax.'
      end
      validate_integer_result(result)
      Converter.to_roman_numeral(result.to_i)
    end
  end
end
