#-------------------------------------------------------------------------------
# Name:        `OS Emergency Service Gazetteer GAWK Script
# Purpose:     `This code is to be used along side the Getting Started Guide
#				which explains the process to use GAWK to split the CSV files
#				by record identifier.
# Created:     `25/03/2024
# Copyright:   `Crown Copyright (c) Ordnance Survey 2014
# Licence:     `THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#               "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#               LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#               FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#               COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#               INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#               BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS
#               OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
#               AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#               OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
#               THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE
#-------------------------------------------------------------------------------

FOR /F %%A IN ('dir *.csv /b/s') DO (CALL :process "%%A" "%%~NA")
@rem -- merge the individual record identifier files
copy *_10_Records.csv Master_10_Records.out
copy *_21_Records.csv Master_21_Records.out
copy *_24_Records.csv Master_24_Records.out
copy *_32_Records.csv Master_32_Records.out
copy *_99_Records.csv Master_99_Records.out
del *_Records.csv
@rem -- add header records to the individual record identifier files
copy Record_10_HEADER_Header.csv+Master_10_Records.out ID10_Header_Records.txt
copy Record_21_BLPU_Header.csv+Master_21_Records.out ID21_BLPU_Records.txt
copy Record_24_LPI_Header.csv+Master_24_Records.out ID24_LPI_Records.txt
copy Record_32_CLASSIFICATION_Header.csv+Master_32_Records.out ID32_Class_Records.txt
copy Record_99_TRAILER_Header.csv+Master_99_Records.out ID99_Trailer_Records.txt
del *_Records.out
@rem -- remove any blank lines from the individual record identifier files
gawk "/./" ID10_Header_Records.txt > ID10_Header_Records.csv
gawk "/./" ID21_BLPU_Records.txt > ID21_BLPU_Records.csv
gawk "/./" ID24_LPI_Records.txt > ID24_LPI_Records.csv
gawk "/./" ID32_Class_Records.txt > ID32_Class_Records.csv
gawk "/./" ID99_Trailer_Records.txt > ID99_Trailer_Records.csv
del *_Records.txt
pause
exit
@rem -- split the source csv into individual files based on the record identifier
:process
SET tempvar1=%~1
SET tempvar2=%~2
gawk < %tempvar1% -F "," "{ if ($1 == \"10\") { print $0 } }" > %tempvar2%_10_Records.csv
gawk < %tempvar1% -F "," "{ if ($1 == \"21\") { print $0 } }" > %tempvar2%_21_Records.csv
gawk < %tempvar1% -F "," "{ if ($1 == \"24\") { print $0 } }" > %tempvar2%_24_Records.csv
gawk < %tempvar1% -F "," "{ if ($1 == \"32\") { print $0 } }" > %tempvar2%_32_Records.csv
gawk < %tempvar1% -F "," "{ if ($1 == \"99\") { print $0 } }" > %tempvar2%_99_Records.csv
GOTO :EOF
