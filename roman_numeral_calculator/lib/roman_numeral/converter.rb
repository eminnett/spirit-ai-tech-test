# frozen_string_literal: true

require_relative './validations'
require 'byebug'

module RomanNumeral
  module Converter
    extend Validations

    NUMERAL_MAPPING = [
      ['M', 1000],
      ['D', 500],
      ['C', 100],
      ['L', 50],
      ['X', 10],
      ['V', 5],
      ['I', 1]
    ]

    def self.to_integer(roman_numeral)
      validate_string(roman_numeral)
      roman_numeral = roman_numeral.strip
      validate_roman_numeral(roman_numeral)

      integer = 0
      letters = roman_numeral.split('')
      letters.each_with_index do |letter, i|
        mapping = NUMERAL_MAPPING.assoc(letter)
        value = mapping[1]

        if i < letters.count - 1
          next_letter = roman_numeral[i + 1]
          next_mapping = NUMERAL_MAPPING.assoc(next_letter)
          if NUMERAL_MAPPING.index(mapping) == NUMERAL_MAPPING.index(next_mapping) + 1
            integer -= value
            next
          end
        end

        integer += value
      end
      integer
    end

    def self.to_roman_numeral(integer)
      validate_integer(integer)
      roman_numeral = ''
      NUMERAL_MAPPING.each_with_index do |(letter, value), i|
        ratio = integer.to_f / value
        leading_five = value.to_s[0] == '5'

        if (leading_five && ratio == 0.8) || (!leading_five && ratio == 0.9)
          next_letter = NUMERAL_MAPPING[i + 1][0]
          roman_numeral += next_letter + letter
          return roman_numeral
        elsif ratio >= 1
          ratio.floor.times do 
            roman_numeral += letter
            integer -= value
          end
          return roman_numeral if integer.zero?
        end
      end
    end
  end
end
