
function Get-Day4-2Solution {
  [CmdletBinding()]
  param (
    # input
    [Parameter()]
    [string]
    $InputValue
  )

  begin {
  }

  process {

    for ($i = 0; ; $i++) {
      $hash = [System.BitConverter]::ToString($md5.ComputeHash($utf8.GetBytes("$($InputValue)$($i)")))
      $trimmedhash = $hash.replace('-', '')


      if ($trimmedhash.Substring(0, 6) -eq '000000') {
        return $i
        break
      }

    }
  }

  end {
  }
}