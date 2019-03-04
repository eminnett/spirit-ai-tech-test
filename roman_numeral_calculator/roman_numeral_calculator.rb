# frozen_string_literal: true

require_relative './lib/roman_numeral/calculator'

puts RomanNumeral::Calculator.evaluate(ARGV[0])
