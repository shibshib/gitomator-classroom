# coding: utf-8
lib = File.expand_path('../lib', __FILE__)
$LOAD_PATH.unshift(lib) unless $LOAD_PATH.include?(lib)
require 'gitomator/classroom/version'

Gem::Specification.new do |spec|
  spec.name          = "gitomator-classroom"
  spec.version       = Gitomator::Classroom::VERSION
  spec.authors       = ["Ala Shaabana"]
  spec.email         = ["ala.shaabana@utoronto.ca"]

  spec.summary       = %q{Automated workflow for software engineering courses}
  spec.description   = %q{Library, scripts and conventions that allow instructors to automate their workflow.}
  spec.homepage      = "https://github.com/CSC301-W2020"
  spec.license       = "MIT"

  spec.files         = `git ls-files -z`.split("\x0").reject { |f| f.match(%r{^(test|spec|features)/}) }
  spec.bindir        = "bin"
  spec.executables   = spec.files.grep(%r{^bin/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  spec.add_development_dependency "bundler", "~> 1.7"
  spec.add_development_dependency "rake", "~> 10.0"
  spec.add_development_dependency "rspec"

  spec.add_runtime_dependency 'gitomator', '>= 0.1.2.3'
  spec.add_runtime_dependency 'trollop', '~> 2.1', '>= 2.1.2'
  spec.add_runtime_dependency 'nokogiri'
end
