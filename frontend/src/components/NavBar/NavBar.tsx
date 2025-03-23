import { Button } from "@/components/ui/button";
import { Avatar, AvatarFallback } from "../ui/avatar";
import { DropdownMenu, DropdownMenuTrigger, DropdownMenuContent, DropdownMenuItem } from "../ui/dropdown-menu";

export default function Navbar() {
  return (
    <nav className="flex items-center justify-between px-6 py-3 bg-background border-b">
      {/* Logo */}
      <div className="text-xl font-bold">DebugMate</div>
      
      {/* Navigation Links */}
      <div className="hidden md:flex space-x-6">
        <Button variant="ghost">Home</Button>
        <Button variant="ghost">Docs</Button>
        <Button variant="ghost">Support</Button>
      </div>
      
      {/* Actions (Theme Toggle & Profile) */}
      <div className="flex items-center space-x-4">
        <DropdownMenu>
          <DropdownMenuTrigger>
            <Avatar>
              <AvatarFallback>DM</AvatarFallback>
            </Avatar>
          </DropdownMenuTrigger>
          <DropdownMenuContent align="end">
            <DropdownMenuItem>Profile</DropdownMenuItem>
            <DropdownMenuItem>Settings</DropdownMenuItem>
            <DropdownMenuItem>Logout</DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
    </nav>
  );
}
