BeforeAll {
    . $PSScriptRoot/day4.ps1

    $Sample = 'abcdef'
    $Sample2 = 'pqrstuv'
}


Describe 'Get-Day4Solution' {
    It 'Starts with five zeroes' {
        $Hash = Get-Day4Solution -InputValue $Sample
        $Hash[1].Substring(0, 7) | Should -Be '00-00-0'
    }

    It 'Provided, abcdef as input, returns 609043' {
        $Solution = Get-Day4Solution -InputValue $Sample
        $Solution[0] | Should -Be 609043
    }

    It 'Provided pqrstuv as input, returns 1048970' {
        $Solution = Get-Day4Solution -InputValue $Sample2

        $Solution[0] | Should -Be 1048970
    }
}