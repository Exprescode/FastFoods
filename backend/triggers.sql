\c cs2102_26

CREATE OR REPLACE FUNCTION check_hours()
    RETURNS TRIGGER
    AS $$
    DECLARE
    myTotalHours int;
    riderType varchar;
    riderId int;
    newHours int;
    BEGIN
      select sum(endhour-starthour) into myTotalHours from intervals where ScheduleId=NEW.ScheduleId;
    	select s.RiderId into riderId from Schedule s where Id = NEW.ScheduleId;
    	select r.EmploymentType into riderType from Riders r where Id=RiderId;
    	
    	newHours := myTotalHours + (NEW.EndHour - NEW.StartHour);
    	
    	IF (riderType = 'part' and newHours > 48) THEN
    	    RAISE EXCEPTION 'Total Hours exceed 48 hours';
    	END IF;
			
    	RETURN NEW;
  END;
    $$ LANGUAGE plpgsql;


create trigger update_hours 
before INSERT ON Intervals
FOR EACH ROW 
EXECUTE PROCEDURE check_hours();   


CREATE OR REPLACE FUNCTION check_hours_and_update_points()
    RETURNS TRIGGER
    AS $$
    DECLARE
    myClosingHours time;
    myOpeningHours time;
    currentPoints int;
    newPoints int;
    BEGIN
      select CloseHour, OpenHour into myClosingHours, myOpeningHours from Restaurants where Id=NEW.RestId;
      
      if (NEW.OrderTime::time > myClosingHours) and (NEW.OrderTime::time < myOpeningHours) THEN
        RAISE EXCEPTION 'STORE IS CLOSED';
      end if;
      
      select points into currentPoints from Customers where Id=NEW.CustId;
      
      newPoints := currentPoints - NEW.PointsUsed;
      
      if (newPoints < 0) then
        RAISE EXCEPTION 'Points used exceed current available points';
      END IF;

      newPoints := currentPoints - NEW.PointsUsed + floor(NEW.Total);
      
      update customers set points=newPoints where Id=NEW.CustId;

    	RETURN NEW;
  END;
    $$ LANGUAGE plpgsql;

create trigger before_new_order 
before INSERT ON Orders
FOR EACH ROW 
EXECUTE PROCEDURE check_hours_and_update_points();   

CREATE OR REPLACE FUNCTION update_item_availability()
    RETURNS TRIGGER
    AS $$
    DECLARE
    myId int;
    myOrderLimit int;
    myCurrentOrders int;
    myNewCurrentOrders int;
    BEGIN
      select fi.OrderLimit, fi.CurrentOrders, fi.Id into myOrderLimit, myCurrentOrders, myId from FoodItems fi, Orders o where fi.name = NEW.name and o.Id = NEW.OrderId  and fi.restId = o.restId;

      myNewCurrentOrders := myCurrentOrders + new.Qty;
      
      If (myNewCurrentOrders > myOrderLimit) then
        RAISE EXCEPTION 'Food Item exceed maximum limit!';
      END IF;
      
      if (myNewCurrentOrders = myOrderLimit) then
        update FoodItems set Availability=false where Id = myId;
      END IF;
      
      update FoodItems set CurrentOrders=myNewCurrentOrders where Id = myId;
      
    	RETURN NEW;
  END;
    $$ LANGUAGE plpgsql;

create trigger check_item_availability
before INSERT ON OrderItems
FOR EACH ROW 
EXECUTE PROCEDURE update_item_availability();   


CREATE OR REPLACE FUNCTION update_commission()
    RETURNS TRIGGER
    AS $$
    DECLARE
    orderCommission float;
    BEGIN
      orderCommission = 0.2 * NEW.total;
      
      update schedule set commission=commission + orderCommission where startdate < NEW.AtCustTime and enddate > NEW.AtCustTime and RiderId=NEW.RiderId;
      
    	RETURN NEW;
  END;
    $$ LANGUAGE plpgsql;

create trigger update_pay
after UPDATE OF AtCustTime ON orders
FOR EACH ROW
EXECUTE PROCEDURE update_commission();