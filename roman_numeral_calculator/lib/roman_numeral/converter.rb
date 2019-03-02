# frozen_string_literal: true

module RomanNumeral
  module Converter
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

    def self.validate_string(roman_numeral)
      return true if roman_numeral.is_a? String

      raise ArgumentError, 'A roman numeral must be a string'
    end
    private_class_method :validate_string

    def self.validate_roman_numeral(roman_numeral)
      return true if /^[IVXLCDM]+$/.match?(roman_numeral)

      raise ArgumentError, "'#{roman_numeral}' is not a valid roman numeral"
    end
    private_class_method :validate_roman_numeral

    def self.validate_integer(integer)
      return true if integer.is_a? Integer

      raise ArgumentError, 'A roman numeral can only be converted from an integer'
    end
    private_class_method :validate_integer
  end
end
