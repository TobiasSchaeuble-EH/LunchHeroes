import { createClient } from '@supabase/supabase-js';

const supabaseUrl = "https://etdodvolyfznkgkwfsuk.supabase.co";
const supabaseAnonKey = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImV0ZG9kdm9seWZ6bmtna3dmc3VrIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTg0OTUwMjIsImV4cCI6MjAxNDA3MTAyMn0.6FBeF5Ng7OfnWsNi_Hq2tDYyS6v-stR6cAoFhAUmuSA";

export const supabase = createClient(supabaseUrl, supabaseAnonKey);