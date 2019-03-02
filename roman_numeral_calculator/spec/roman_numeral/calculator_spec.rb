# frozen_string_literal: true

require_relative '../spec_helper'
require_relative '../../lib/roman_numeral/calculator'

module RomanNumeral
  RSpec.describe Calculator do
    describe '.evaluate' do
      context 'when given a calculable roman numeral mathematical expression' do
        it 'does not yet do anything useful' do
          expect(Calculator.evaluate('V + IV')).to eq('V + IV')
        end
      end

      context 'when given an expression with unexpected characters' do
        it 'raises an error' do
          bad_inputs = ['foo', 'T+K']
          bad_inputs.each do |input|
            expect { Calculator.evaluate(input) }.to raise_error(ArgumentError)
          end
        end
      end
    end
  end
end
