# frozen_string_literal: true

module RomanNumeral
  module Validations
    def validate_expression(expression)
      return true if %r{^[IVXLCDM\(\)\^/\*\+\-\s]+$}.match?(expression)

      raise ArgumentError, "'#{expression}' is not a calculable expression"
    end

    def validate_string(roman_numeral)
      return true if roman_numeral.is_a? String

      raise ArgumentError, 'A roman numeral must be a string'
    end

    def validate_roman_numeral(roman_numeral)
      return true if /^[IVXLCDM]+$/.match?(roman_numeral)

      raise ArgumentError, "'#{roman_numeral}' is not a valid roman numeral"
    end

    def validate_integer(integer)
      return true if integer.is_a? Integer

      raise ArgumentError, 'A roman numeral can only be converted from an integer'
    end
  end
end
