#!/usr/bin/env ruby

require "yaml"

ARGV.each do |path|
  YAML.load_file(path, aliases: true)
end
