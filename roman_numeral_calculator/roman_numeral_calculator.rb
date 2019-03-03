# frozen_string_literal: true

require 'slop'
require_relative './lib/roman_numeral/calculator'

puts RomanNumeral::Calculator.evaluate(ARGV[0])
