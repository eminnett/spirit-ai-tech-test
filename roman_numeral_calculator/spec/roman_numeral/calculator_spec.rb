# frozen_string_literal: true

require_relative '../spec_helper'
require_relative '../../lib/roman_numeral/calculator'

module RomanNumeral
  RSpec.describe Calculator do
    describe '.evaluate' do
      it 'does not yet do anything useful' do
        expect(Calculator.evaluate('foo')).to eq('foo')
      end
    end
  end
end
