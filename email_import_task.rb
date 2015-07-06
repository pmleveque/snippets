
namespace :imports do
  desc ""

  task :txt => :environment do
    person = Person.new

    Dir.open(File.join(Rails.root, "lib/tasks/Roca")).each do |file|
      Person.transaction do
        if file.scan(/txt/) != []
          puts "\n\n\n-------------------FILE: #{file} -------------------------"
          #code = file.scan(/BJ.-.(.*).utf8/)[0][0]
          File.open(File.join(Rails.root, "lib/tasks/Roca", file), "r").each do |line|
            person = Person.new
            person.email = line.gsub("\n","").gsub("\r","")
            if person.email.match(/^(|(([A-Za-z0-9]+_+)|([A-Za-z0-9]+\-+)|([A-Za-z0-9]+\.+)|([A-Za-z0-9]+\++))*[A-Za-z0-9]+@((\w+\-+)|(\w+\.))*\w{1,63}\.[a-zA-Z]{2,6})$/i).nil?
              puts "XXXX", person.email
            else
              puts person.email
              person.save
            end
          end
        end
      end
    end

  end

  task :xls => :environment do


    Dir.open(File.join(Rails.root, "lib/tasks/Roca")).each do |file|
      if file.scan(/xls/) != []
        puts "-----------------FILE: #{file}-------------------"
        #code = file.scan(/BJ.-.(.*).utf8/)[0][0]
        book = Spreadsheet.open(File.join(Rails.root, "lib/tasks/Roca", file), "r")
        book.worksheets.each do |worksheet|
          worksheet.each do |row|
            puts "---- #{row[0]} --- #{row[1]} --- #{row[2]}"

            if row[0].nil?
              puts "row0 = nil"
            else
              emails = []
              emails << row[0]
              emails << row[0].to_s.gsub(" ","").gsub("\n","").gsub("\r","")
              emails << row[0].to_s.match("<(.*)>")[1] unless row[0].to_s.match("<(.*)>").nil?
              emails << row[1]
              emails << row[2]

              person = Person.new

              emails.compact.each do |email|
                person.email = email unless email.to_s.match(/^(|(([A-Za-z0-9]+_+)|([A-Za-z0-9]+\-+)|([A-Za-z0-9]+\.+)|([A-Za-z0-9]+\++))*[A-Za-z0-9]+@((\w+\-+)|(\w+\.))*\w{1,63}\.[a-zA-Z]{2,6})$/i).nil?
              end

              unless person.email.nil?
                person.save
                puts person.email
              end
            end

          end
        end
      end
    end

  end
end