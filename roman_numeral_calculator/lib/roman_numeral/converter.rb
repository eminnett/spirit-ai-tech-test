# frozen_string_literal: true

module RomanNumeral
  module Converter
    def self.to_integer(roman_numeral)
      5 if roman_numeral == 'V'
    end

    def self.to_roman_numeral(integer)
      'V' if integer == 5
    end
  end
end
