{
  description = "python 3.11.2 met juiste libs";
  inputs = 
  {
      nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
#     python3112.url = "github:nixos/nixpkgs/96ba1c52e54e74c3197f4d43026b3f3d92e83ff9";
  };
  outputs = { self, nixpkgs, ... }@inputs:
    let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
    in
    {
      devShells.x86_64-linux.default =
      pkgs.mkShell
      {
        nativeBuildInputs = with pkgs; [
          cowsay #voor funny redenen
          jetbrains.pycharm-community
#         inputs.python3112.legacyPackages.${system}.python311
#         inputs.python3112.legacyPackages.${system}.python311Packages.matplotlib
#         inputs.python3112.legacyPackages.${system}.python311Packages.numpy  
        ];
    
    shellHook = ''
    cowsay "welcom to pycharm shell"
    pycharm-community
    '';
      };
    };
  }
