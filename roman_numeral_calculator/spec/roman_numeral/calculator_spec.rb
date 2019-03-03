# frozen_string_literal: true

require_relative '../spec_helper'
require_relative '../../lib/roman_numeral/calculator'

# nodoc
module RomanNumeral
  RSpec.describe Calculator do
    describe '.evaluate' do
      calculations = [
        ['V + IV', 'IX'],
        ['V + IX', 'XIV'],
        ['XIX - X', 'IX'],
        ['XIX - I', 'XVIII'],
        ['(V + IX) * III', 'XLII'],
        ['V + IX * III', 'XXXII'],
        ['VI / II + IX * III', 'XXX'],
        ['IV / V * X', 'VIII'],
        ['III^IV', 'LXXXI'],
        ['III**IV', 'LXXXI']
      ]

      context 'when given a calculable roman numeral mathematical expression' do
        calculations.each do |(expression, expectation)|
          it "evaluates #{expression} as #{expectation}" do
            expect(Calculator.evaluate(expression)).to eq(expectation)
          end
        end

        context 'and the result is not an integer' do
          it 'raises an error' do
            bad_inputs = ['V / IV']
            bad_inputs.each do |input|
              expect { Calculator.evaluate(input) }.to raise_error(ArgumentError)
            end
          end
        end
      end

      context 'when given an unevaluatable expression' do
        it 'raises an error' do
          bad_inputs = ['((V + IV)', '+ V - I']
          bad_inputs.each do |input|
            expect { Calculator.evaluate(input) }.to raise_error(ArgumentError)
          end
        end
      end

      context 'when given an expression with unexpected characters' do
        it 'raises an error' do
          bad_inputs = ['foo', 'T+K', 'V + 5']
          bad_inputs.each do |input|
            expect { Calculator.evaluate(input) }.to raise_error(ArgumentError)
          end
        end
      end
    end
  end
end
