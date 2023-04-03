

function Get-Day4Solution {
    [CmdletBinding()]
    param (
        # input
        [Parameter()]
        [string]
        $InputValue
    )

    begin {
        [int]$number = 0
    }

    process {
        do {
            $number++
            $combinedString = $InputValue + $number.ToString()

            $md5 = New-Object -TypeName System.Security.Cryptography.MD5CryptoServiceProvider
            $utf8 = New-Object -TypeName System.Text.UTF8Encoding
            $hash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes($combinedString)))
            $trimmedhash = $hash.replace('-', '')



            } until (
                #Untill the value is correct
                $trimmedhash.Substring(0,5) -eq '00000'
            )
        }

        end {
            return $number, $hash
        }
    }