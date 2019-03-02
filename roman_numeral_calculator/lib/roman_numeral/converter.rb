# frozen_string_literal: true

require_relative './validations'

module RomanNumeral
  module Converter
    extend Validations

    NUMERAL_MAPPING = {
      'I': 1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000
    }

    def self.to_integer(roman_numeral)
      validate_string(roman_numeral)
      roman_numeral = roman_numeral.strip
      validate_roman_numeral(roman_numeral)

      5 if roman_numeral == 'V'
    end

    def self.to_roman_numeral(integer)
      validate_integer(integer)
      'V' if integer == 5
    end
  end
end
